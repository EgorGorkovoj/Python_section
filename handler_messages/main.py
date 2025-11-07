from parser import MattermostParser, SlackParser, TelegramParser

from data_message import JsonMessage, MessageType
from fabric import MessageParserFabric

JSON = {"channel": "dev", "user": "alex", "message": "Привет!"}


def main():
    MessageParserFabric.register_parser(MessageType.TELEGRAM, TelegramParser)
    MessageParserFabric.register_parser(
        MessageType.MATTERMOST, MattermostParser
    )
    MessageParserFabric.register_parser(MessageType.SLACK, SlackParser)
    json_telegram = JsonMessage(
        message_type=MessageType.TELEGRAM, payload=JSON
    )
    json_mattermost = JsonMessage(
        message_type=MessageType.MATTERMOST, payload=JSON
    )
    json_slack = JsonMessage(message_type=MessageType.SLACK, payload=JSON)
    fabric = MessageParserFabric()
    parser_tg = fabric.get_parser(json_telegram)
    parser_mattermost = fabric.get_parser(json_mattermost)
    parser_slack = fabric.get_parser(json_slack)
    print(parser_tg.parse())
    print(parser_mattermost.parse())
    print(parser_slack.parse())


if __name__ == "__main__":
    main()
