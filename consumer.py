import pika

credentials = pika.PlainCredentials("guest", "guest")
conn_params = pika.ConnectionParameters("localhost",
                                       credentials = credentials)
conn_broker = pika.BlockingConnection(conn_params)

channel = conn_broker.channel()
channel.exchange_declare(exchange = "first-exchange",
                         exchange_type = "direct",
                         passive = False,
                         durable = True,
                         auto_delete = False)

channel.queue_declare(queue = "first-queue")
channel.queue_bind(queue = "first-queue",
                   exchange = "first-exchange",
                   routing_key = "hola")

def msg_consumer(chanel, method, header, body):
    channel.basic_ack(delivery_tag = method.delivery_tag)
    if body == "quit":
        channel.basic_cancel(consumer_tag = "first-consumer")
        channel.stop_consuming()
    else:
        print body
    return

channel.basic_consume(msg_consumer,
                      queue = "first-queue",
                      consumer_tag = "first-consumer")

channel.start_consuming()
