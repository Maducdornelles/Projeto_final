# pubsub.py
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

class AsyncConn:
    def __init__(self, id: str, channel_name: str) -> None:
        config = PNConfiguration()
        config.subscribe_key = 'sub-c-386a1c65-dd4c-49ab-8117-a504817ae857'
        config.publish_key = 'pub-c-7154fd8e-d85c-48d1-94c2-cb0f5b2d156f'
        config.secret_key = 'sec-c-NjQ1ZjZkMjktZGZmZS00M2Q2LWI1YmMtZDE1NzcxNDkzNjAx'
        config.user_id = id
        config.enable_subscribe = True
        config.daemon = True

        self.pubnub = PubNub(config)
        self.channel_name = channel_name

        print(f"Configurando conexão com o canal '{self.channel_name}'...")
        subscription = self.pubnub.channel(self.channel_name).subscription()
        subscription.subscribe()

    def publish(self, data: dict):
        print("Publicando mensagem no PubNub...")
        self.pubnub.publish().channel(self.channel_name).message(data).sync()
