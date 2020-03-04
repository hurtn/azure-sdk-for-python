# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_detect_language.py

DESCRIPTION:
    This sample demonstrates how to detect language in a batch of different
    documents.

USAGE:
    python sample_detect_language.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_TEXT_ANALYTICS_ENDPOINT - the endpoint to your cognitive services resource.
    2) AZURE_TEXT_ANALYTICS_KEY - your text analytics subscription key
"""

import os


class DetectLanguageSample(object):

    endpoint = os.getenv("AZURE_TEXT_ANALYTICS_ENDPOINT")
    key = os.getenv("AZURE_TEXT_ANALYTICS_KEY")

    def detect_language(self):
        # [START batch_detect_language]
        from azure.ai.textanalytics import TextAnalyticsClient, TextAnalyticsApiKeyCredential
        text_analytics_client = TextAnalyticsClient(endpoint=self.endpoint, credential=TextAnalyticsApiKeyCredential(self.key))
        documents = [
            "This document is written in English.",
            "Este es un document escrito en Español.",
            "这是一个用中文写的文件",
            "Dies ist ein Dokument in englischer Sprache.",
            "Detta är ett dokument skrivet på engelska."
        ]

        result = text_analytics_client.detect_language(documents)

        for idx, doc in enumerate(result):
            if not doc.is_error:
                print("Document text: {}".format(documents[idx]))
                print("Language detected: {}".format(doc.primary_language.name))
                print("ISO6391 name: {}".format(doc.primary_language.iso6391_name))
                print("Confidence score: {}\n".format(doc.primary_language.score))
            if doc.is_error:
                print(doc.id, doc.error)
        # [END batch_detect_language]


if __name__ == '__main__':
    sample = DetectLanguageSample()
    sample.detect_language()
