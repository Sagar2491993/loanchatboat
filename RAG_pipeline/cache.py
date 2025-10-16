import os
import json
import hashlib
from datetime import datetime

class ResponseCache:
    """
    Simple JSON-based cache system for storing and retrieving
    responses to repeated user questions in RAG pipeline.
    """

    def __init__(self, cache_file="cache_store.json"):
        self.cache_path = os.path.join(
            os.path.dirname(__file__), cache_file
        )
        self.cache = self._load_cache()

    def _load_cache(self):
        """Load existing cache from disk."""
        if os.path.exists(self.cache_path):
            try:
                with open(self.cache_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def _save_cache(self):
        """Persist cache to disk."""
        try:
            with open(self.cache_path, "w", encoding="utf-8") as f:
                json.dump(self.cache, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f" Failed to save cache: {e}")

    def _hash_question(self, question):
        """Generate a consistent hash for each unique question."""
        return hashlib.sha256(question.lower().strip().encode()).hexdigest()

    def get(self, question):
        """Retrieve cached response if available."""
        key = self._hash_question(question)
        entry = self.cache.get(key)
        if entry:
            print(" Using cached response")
            return entry["answer"]
        return None

    def add(self, question, answer):
        """Store new question-answer pair to cache."""
        key = self._hash_question(question)
        self.cache[key] = {
            "question": question,
            "answer": answer,
            "timestamp": datetime.now().isoformat()
        }
        self._save_cache()
