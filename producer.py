import pika, sys

"""build connection"""
credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost",
                                       credentials = credentials)
conn_broker = pika.BlockingConnection(conn_params)

"""get channel"""
channel = conn_broker.channel()

"""declare exchange"""
channel.exchange_declare(exchange = "first-exchange",
                         exchange_type = "direct",
                         passive = False,
                         durable = True,
                         auto_delete = False)

msg = sys.argv[1]
msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"


"""publish message"""
channel.basic_publish(body = msg,
                      exchange = "first-exchange",
                      properties = msg_props,
                      routing_key = "hola")

