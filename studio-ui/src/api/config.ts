// Single source of truth for where requests go and which model they ask for.
// ponytail: fixed URL, no env override. Add VITE_API_URL when the API is hosted elsewhere.
export const BASE_URL = "http://localhost:8000";
export const DEFAULT_MODEL = "gemini-4-hydrogen";
export const DEFAULT_THINKING = "low";
