# utils/evidence_manager.py
import pandas as pd
from datetime import datetime, timedelta

class EvidenceManager:
    def __init__(self):
        self.evidence_store = []

    def store_evidence(self, requirement_id, uploaded_file):
        """Store evidence for a requirement"""
        evidence_record = {
            "requirement_id": requirement_id,
            "filename": uploaded_file.name,
            "upload_date": datetime.now(),
            "file_type": uploaded_file.type,
            "status": "uploaded"
        }
        self.evidence_store.append(evidence_record)
        return True

    def get_evidence_stats(self):
        """Get evidence statistics"""
        total = len(self.evidence_store)
        expiring_soon = 0  # Would calculate based on expiry dates
        missing = 10 - total  # Mock - assume 10 requirements need evidence
        
        return {
            "total": total,
            "expiring_soon": expiring_soon,
            "missing": missing
        }

    def get_evidence_dataframe(self):
        """Convert evidence store to DataFrame for display"""
        if not self.evidence_store:
            return pd.DataFrame(columns=["requirement_id", "filename", "upload_date", "status"])
        
        return pd.DataFrame(self.evidence_store)