from google.cloud import firestore

from static_data import ALIENS

PROJECT_NAME = 'mikes-demo2023'
COLLECTION_NAME = 'mikes_aliens'


def create_some_documents():
    firestore_client = firestore.Client(project=PROJECT_NAME)
    transaction = firestore_client.transaction()
    for alien in ALIENS:
        doc_key = alien.replace(' ', '')
        print(f"Now set document {alien}")
        fsdocument = firestore_client.collection(COLLECTION_NAME).document(doc_key)
        transaction.set(fsdocument,
                        {
                            "houseColor": firestore.ArrayUnion(['yellow', 'orange']),
                            'alien_name': alien}
                        , merge=True)

    transaction.commit()


if __name__ == '__main__':
    create_some_documents()
