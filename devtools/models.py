from django.db import models
from typing import Any

# Create your models here.

class DevTool(models.Model):
    """ 
    Represents a development tool e.g Postman
    """
    name: str = models.CharField(
            max_length=100, unique=True, help_text="Name of the development tool"
            )
    description: str | None = models.TextField(
           blank=True, null=True, help_text="A short description of the tool"
           )
    website: str = models.URLField(
            help_text="Official website of the tool or documentation URL"
            )
    added_on: Any = models.DateTimeField(
            auto_now_add=True, help_text="Time when the tool was first added"
            )
    updated_on: Any = models.DateTimeField(
            auto_now=True, help_text="Time when the tool data was last updated"
            )

    def __str__(self) -> str:
        return f"{self.name}"
