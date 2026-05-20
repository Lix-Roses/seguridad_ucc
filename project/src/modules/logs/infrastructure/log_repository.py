from src.modules.logs.domain.log_entity import SystemLog

class LogRepository:

    @staticmethod
    def create(db, log):
        db.add(log)
        db.commit()
        db.refresh(log)
        return log