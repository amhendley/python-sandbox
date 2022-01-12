# Python Sandbox

## AWS

### Latest ECR repository version

> aws/get_latest_ecr_version.py

Great for when you use the immutable tag `latest` that shifts to the
next newer version of a repository image.

## Encryption

### PGP
> encryption/create_pgp_keys.py
> 
> encryption/file_decrypt_pgp.py
> 
> encryption/file_encrypt_pgp.py

### RSA
> encryption/create_rsa_keys.py
> 
> encryption/file_decrypt_rsa.py
> 
> encryption/file_encrypt_rsa.py

## JSON

### JSON schema validation

> json/json_validation.py
> 
> json/json_validation_extended.py
 
Examples of validating a JSON object using JSON schema definitions.

## JWT

### Create a new JWT

> jwt/create_jwt_token.py

Example of the creation of a Java Web Token (JWT) using a configuration
dictionary.

> jwt/read_validate_jwt_token.py

Using the token generated from above, or anywhere really, this script
demonstrates how to validate a JWT.

## Networking

> networking/chat_server.py
> 
> networking/echo_client.py
> 
> networking/echo_server.py
> 
> networking/epoll_server.py
> 
> networking/forked_server.py
> 
> networking/host.py
> 
> networking/threading_server.py


## TOML

### TOML reader

> toml/toml_reader.py

Example of reading a TOML configuration file.

### TOML writer

> toml/toml_writer.py

Example of creating a TOML configuration file from a data dictionary
using the `rtoml` package and then re-opening.

## PDF's

> combine_pdfs.py
>
> create_pdf.py
>
> rotate_first_page.py
>
> split_half_half.py

Examples of manipulating PDF documents using the `borb` package.

## Miscellaneous

### No conditionals

> misc/no_conditions.py

How to remove the over usage of conditionals

### Enumerators

> misc/using_enums.py

Example of how to establish enumerator classes

### Data classes

> misc/using_dataclass.py

Example of using the `dataclasses.dataclass` class.

### All and Any

> misc/check_required_keys_exist_in_a_dict.py

Examples of how and when to use the `all` or `any` function.
