# CREW_AI
# 📺 YouTube Transcript Crawler with Embedchain

This project fetches transcripts from YouTube videos using the [`youtube-transcript-api`](https://github.com/jdepoix/youtube-transcript-api), with support for integrating them into Embedchain-powered LLM apps.

---

## 🚀 Features

- ✅ Automatically fetch video transcripts from YouTube URLs
- ✅ Supports full channel/playlist crawling
- ✅ Integrates with [Embedchain](https://github.com/embedchain/embedchain)
- ✅ Uses LangChain-compatible format for building RAG apps
- ⚠️ Handles YouTube's rate limits (`429 Too Many Requests`)

---

## 📦 Requirements

> Python 3.9 or above is recommended.

Install dependencies:

```bash
pip install -r requirements.txt
