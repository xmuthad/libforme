import json, smtplib
import pika

if __name__ == '__main__':
    AMQP_SERVER = 'localhost'

AMQP_USER = 'alert_user'
AMQP_PASS = 'alertme'
AMQP_VHOST = '/'
AMQP_EXCHANGE = 'alerts'

creds_broker = pika.PlainCredentials(AMQP_USER, AMQP_PASS)
conn_params = pika.ConnectionParameters(AMQP_SERVER,
                                        virtual_host = AMQP_VHOST,
                                        credentials = creds_broker)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()
