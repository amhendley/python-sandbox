#!/usr/bin/env python3

from typing import List
import boto3
import click


def get_session(role_arn, session_name, region_name):
    sts_client = boto3.client('sts')

    if role_arn:
        response = sts_client.assume_role(
            RoleArn=role_arn,
            RoleSessionName=session_name
        )

        session = boto3.Session(
            aws_access_key_id=response['Credentials']['AccessKeyId'],
            aws_secret_access_key=response['Credentials']['SecretAccessKey'],
            aws_session_token=response['Credentials']['SessionToken'],
            region_name=region_name
        )
    else:
        session = boto3.session()

    return session


def get_digest_versions(response):
    digest_versions = {}

    digests: List[str] = sorted(set([image['imageDigest']
                                     for image in response['imageIds']]))
    for digest in digests:
        digest_versions[digest] = [image['imageTag']
                                   for image in response['imageIds']
                                   if image['imageDigest'] == digest]

    return digest_versions


def get_latest_ecr_version(session, repository_name: str):
    ecr_client = session.client('ecr')

    response = ecr_client.list_images(
        repositoryName=repository_name,
        filter={'tagStatus': 'TAGGED'},
        maxResults=50
    )

    digest_versions = {}
    next_token = response['nextToken'] if 'nextToken' in response else None
    while next_token is not None:
        digest_versions = {**digest_versions, **get_digest_versions(response)}
        response = ecr_client.list_images(
            repositoryName=repository_name,
            filter={'tagStatus': 'TAGGED'},
            nextToken=next_token,
            maxResults=50
        )
        next_token = response['nextToken'] if 'nextToken' in response else None
    digest_versions = {**digest_versions, **get_digest_versions(response)}

    versions: List[str] = [version
                           for digest, versions in digest_versions.items()
                           if 'latest' in versions
                           for version in versions
                           if version != 'latest']

    return sorted(set(versions), reverse=True)[0]


@click.group()
@click.pass_context
@click.option('--repository', required=True, type=click.STRING,
              help='The fully path name of the ECR repository')
@click.option('--role-arn', required=False, type=click.STRING,
              help='The fully qualified ARN fo the role to assume')
@click.option('--region', required=False, type=click.STRING,
              help='The AWS region to use querying the ECR')
@click.option('--output', required=False, type=click.STRING,
              help='Optional path to an output file')
def main(ctx, repository, role_arn, region, output):
    session = get_session(
        role_arn=role_arn,
        session_name=f'',
        region_name=region
    )
    result = get_latest_ecr_version(repository_name=repository, session=session)

    if output:
        with open(file=output, mode='w') as file:
            file.writelines(result)

    ctx.data['latest_version'] = result
    return result


if __name__ == '__main__':
    data = {}
    result = main(data)
    print(data['latest_version'])
