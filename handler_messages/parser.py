from abc import ABC, abstractmethod

from data_message import JsonMessage, ParsedMessage


class Parser(ABC):

    def __init__(self, json_obj: JsonMessage):
        self.json_obj = json_obj

    @abstractmethod
    def parse(self):
        pass


class TelegramParser(Parser):

    def parse(self):
        return ParsedMessage(
            source=self.json_obj.message_type,
            data=self.json_obj.payload,
        )


class MattermostParser(Parser):

    def parse(self):
        return ParsedMessage(
            source=self.json_obj.message_type,
            data=self.json_obj.payload,
        )


class SlackParser(Parser):

    def parse(self):
        return ParsedMessage(
            source=self.json_obj.message_type,
            data=self.json_obj.payload,
        )
