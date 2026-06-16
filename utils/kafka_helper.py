import json
from confluent_kafka import Consumer, KafkaError
def get_latest_kafka_message(topic, bootstrap_servers="localhost:9092", group_id="qa_automation_group"):
    # 1. Configure the Consumer
    consumer_config = {
        'bootstrap.servers': bootstrap_servers,
        'group.id': group_id,
        'auto.offset.reset': 'latest' # We only want new messages generated during our test
    }
    consumer = Consumer(consumer_config)
    consumer.subscribe([topic])
    print(f"\n[Kafka] Listening to topic: {topic}...")
    # 2. Poll for messages (Wait up to 10 seconds for the UI event to process)
    msg = consumer.poll(timeout=10.0)
    consumer.close()
    # 3. Handle the result
    if msg is None:
        return None # No message received within timeout
    if msg.error():
        raise KafkaError(msg.error())
    # Decode the binary payload into a Python Dictionary
    payload = json.loads(msg.value().decode('utf-8'))
    return payload