from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

db = SQLAlchemy()

class SeoResult(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    url: Mapped[str] = mapped_column(String(500), nullable=False)
    title: Mapped[str] = mapped_column(String(200))
    meta_description: Mapped[str] = mapped_column(Text)
    h1_header: Mapped[str] = mapped_column(String(200))
    h2_headers: Mapped[str] = mapped_column(Text) # Storing as a comma-separated string
    word_count: Mapped[int] = mapped_column(Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "url": self.url,
            "title": self.title,
            "meta_description": self.meta_description,
            "h1_header": self.h1_header,
            "h2_headers": self.h2_headers.split(',') if self.h2_headers else [],
            "word_count": self.word_count
        }
