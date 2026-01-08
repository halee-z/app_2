"""
WSGI entry point for Vercel serverless deployment.
Vercel automatically loads this file for Python projects.
"""
from src.main import app

# Vercel requires this to be the exported ASGI application
# For WSGI compatibility with serverless functions
__all__ = ["app"]
