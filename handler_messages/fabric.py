from parser import Parser

from data_message import JsonMessage, MessageType


class MessageParserFabric:

    _register_parser: dict[MessageType, type[Parser]] = {}

    @classmethod
    def register_parser(cls, message_type: MessageType, parser: type[Parser]):
        cls._register_parser[message_type] = parser

    @classmethod
    def get_parser(self, json_message: JsonMessage) -> Parser:
        parser = MessageParserFabric._register_parser.get(
            json_message.message_type
        )
        if not parser:
            raise ValueError("Такого парсера не существует!")
        return parser(json_obj=json_message)
