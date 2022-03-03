# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker ,FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
from databaseintegeration import DataUpdate
from rasa_sdk.types import DomainDict

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
            return "action_submit"
        async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

            DataUpdate(tracker.get_slot("requirement")
            ,tracker.get_slot("mockup")
            ,tracker.get_slot("url")
            ,tracker.get_slot("timeline")
            ,tracker.get_slot("budget")
            ,tracker.get_slot("name")
            ,tracker.get_slot("email")
            ,tracker.get_slot("phone"))
            dispatcher.utter_message("Thanks for the valuable information. ")
            return() 

class ValidateName(FormValidationAction):

    def name(self) -> Text:

        return "validate_info_form"


    # def validate_first_name_last_name(
    #     self,
    #     slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `first_name` value."""
    #     print(f"First name given = {slot_value} length = {len(slot_value)}")
    #     if len(slot_value) <= 2:
    #         dispatcher.utter_message(text=f"That's a very short name. I'm assuming you mis-spelled.")
    #         return {"first_name_last_name": None}
    #     else:
    #         return {"first_name_last_name": slot_value}
    # def validate_acedamicyear(
    #     self,
    #     slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #    if slot_value == "2021":
           
    #        return{"acedamicyear": slot_value}

    #    else:
    #        dispatcher.utter_message(text="Please select current year")
    #        return {"acedamicyear": None}    
