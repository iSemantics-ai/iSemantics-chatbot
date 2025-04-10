# 🕸 ️iSemantics Chatbot (WhatsApp)

This project is a complete pipeline that scrapes our company data from our website, chunks the content, stores it in a vector database, and integrates with a chatbot on WhatsApp. The chatbot uses the embedded knowledge to respond intelligently to user queries based on the website content.
## ✨ Features

- 🌐 Web Scraping: Automatically extracts content from the company website.

- 🧩 Chunking & Embedding: Processes and chunks scraped data for efficient storage and retrieval.

- 🧠 Vector Store: Stores processed data using vector embeddings for semantic search.

- 🤖 Chatbot: Uses retrieved information to answer queries via natural language.

- 📲 WhatsApp Integration: Fully integrated with WhatsApp for user interactions.

## 🧠 How It Works

- Scrape: The site content is scraped recursively (or by sitemap).

- Chunk: Long content is split into manageable chunks (e.g., 500 tokens with overlap).

- Embed: Each chunk is converted into a vector embedding.

- Store: Vectors are stored in a vector database for fast semantic retrieval.

- Query: Incoming user messages are embedded and matched against the stored chunks.

- Respond: The chatbot formulates a response using the retrieved chunks as context.

## 📈 Use Cases

- Automated customer support

- Company knowledgebase access via WhatsApp

- Sales assistant bot for product information

- Internal helpdesk for employee FAQs
