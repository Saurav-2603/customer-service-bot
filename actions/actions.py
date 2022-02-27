# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet, EventType

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "user_detail_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # buttons=[
        #     {"payload":"/mockup{'mck':'Basic Requirements'}","title":"mockup"},
        #     {"payload":"","title":"timeline"},
        #     {"payload":"","title":"budget"},
        #     {"payload":"","title":"menu"},
        #     {"payload":"","title":""},
        #     {"payload":"","title":""},
        # ]
        required_slots=["requirement","mockup","url","timeline","budget","name","email","phone"]

        for slot_name in required_slots:
            if  tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot",slot_name)]
            
        return [SlotSet("requested_slot",None)]
        

        # dispatcher.utter_message(text="Hello World!")

    class ActionSubmit(Action):
        def name(self) -> Text:
            return "validate_name_form"
        def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            dispatcher.utter_message(template="utter_lead_q2",req = tracker.get_slot("requirement")
            ,mock = tracker.get_slot("mockup")
            ,ur = tracker.get_slot("url")
            ,tim = tracker.get_slot("timeline")
            ,bud = tracker.get_slot("budget")
            ,nam = tracker.get_slot("name")
            ,ema = tracker.get_slot("email")
            ,pho = tracker.get_slot("phone"))
