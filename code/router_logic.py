"""
Example Router LLM orchestration logic used in the MİHMANDAR system.

This example demonstrates how user queries are classified
and routed to specialized AI agents.
"""

class HospitalAssistant:

    def __init__(self):

        self.agents = {
            "hospital_info": InformationAgent(),
            "navigation": NavigationAgent(),
            "patient_query": AppointmentAgent()
        }

    def route_query(self, user_query):

        # Router LLM analyzes user intent
        intent = router_llm(user_query)

        print(f"[Router Decision]: {intent}")

        # Forward request to related agent
        if intent in self.agents:
            return self.agents[intent].run(user_query)

        return "Unable to process request."


# Example usage
query = "Where is the cardiology department?"
response = HospitalAssistant().route_query(query)
