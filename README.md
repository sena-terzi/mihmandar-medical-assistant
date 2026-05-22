# MİHMANDAR

LLM-based multi-agent hospital assistant system for patient guidance, appointment management, and smart hospital navigation.

---

## Overview

MİHMANDAR is an AI-powered medical communication and navigation assistant designed for hospital environments.

The system enables patients to:
- Access hospital-related information
- Manage appointment workflows
- Navigate inside the hospital
- Interact through natural language

The architecture is based on a Router LLM that routes user queries to specialized AI agents.

---

## System Architecture

<p align="center">
  <img src="assets/architecture.png" width="700"/>
</p>

The Router LLM analyzes the user intent and forwards the request to the appropriate agent:

- Information Agent
- Appointment Agent
- Navigation Agent

This modular design allows scalable and extensible hospital assistant services.

---

## Features

- Multi-agent LLM architecture
- Intent routing using Router LLM
- Natural language interaction
- Hospital information assistance
- Appointment workflow management
- Indoor navigation support
- Modular and extensible system design

---

## Example Queries

```text
"Where is the cardiology department?"
"I want to book an appointment for tomorrow."
"How can I reach the MRI unit?"
```

---

## Tech Stack

- Python
- FastAPI
- LLM APIs
- NLP
- Vector Search
- Gradio / Web UI

---

## Project Structure

```text
mihmandar/
│
├── agents/
├── assets/
├── app.py
├── router.py
├── requirements.txt
└── README.md
```

---

## Future Improvements

- Voice-based interaction
- Real-time indoor map integration
- RAG-based medical document retrieval
- Multilingual support
- Mobile application integration

---

## Note

Some production integrations and private components are not included in the public repository.
