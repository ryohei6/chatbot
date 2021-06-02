# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from typing import Any, Text, Dict, List

from rasa_core_sdk import Action
from rasa_sdk import Tracker
from rasa_core_sdk.events import SlotSet

class ActionRegister(Action):
    def name(self):
        return 'action_register'

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text = "こちらから登録いただけます。")
        dispatcher.utter_message(text = "https://grp01.id.rakuten.co.jp/rms/nid/registfwd")
        return []


class ActionLeave(Action):
    def name(self):
        return 'action_leave'

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text = "こちらの注意事項をよく読み、リンク先より退会の手続きをお願いいたします。")
        dispatcher.utter_message(text = "https://ichiba.faq.rakuten.net/detail/000011326")
        return []

class ActionChangeAgeOrSex(Action):
    def name(self):
        return 'action_change_age_or_sex'

    def run(self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text = "年齢や性別の変更を行うことはできません。")
        dispatcher.utter_message(text = "詳細につきましては以下のリンクをご参照ください。")
        dispatcher.utter_message(text = "https://ichiba.faq.rakuten.net/detail/000006520")
        return []