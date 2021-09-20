from enum import Enum
from typing import Union


class MessagePriority(Enum):
    """
    Message Priority enumerator
    """
    Low = 0
    Medium = 1
    High = 2

    @classmethod
    def parse(cls, value: Union[str, int]):
        """
        Evaluates the values passed as a MessagePriority value

        :param value: The value to evaluate
        :return: A MessagePriority value
        """
        if isinstance(value, str):
            if 'low' == value.lower():
                return MessagePriority.Low
            elif 'medium' == value.lower():
                return MessagePriority.Medium
            elif 'high' == value.lower():
                return MessagePriority.High
            else:
                raise ValueError(f'Unable to parse value {value} to a MessagePriority')
        elif isinstance(value, int):
            if value == 0:
                return MessagePriority.Low
            elif value == 1:
                return MessagePriority.Medium
            elif value == 2:
                return MessagePriority.High
            else:
                raise ValueError(f'Unable to parse value {value} to a MessagePriority')
        else:
            raise ValueError(f'Unable to parse value type {type(value)} to a MessagePriority')


p = MessagePriority.parse(2)
print(p)

p = MessagePriority.parse('Low')
print(p)

p = MessagePriority.parse(True)
print(p)

# p = MessagePriority.parse(b'low')
# print(p)

p = MessagePriority.parse(1.2)
print(p)
