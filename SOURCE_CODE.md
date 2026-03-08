# CashMeIfYouCan - Source Code Information

## Repository Access
**GitHub Repository**: [https://github.com/Bababushka/CCD-Credit-Scoring-System.git](https://github.com/Bababushka/CCD-Credit-Scoring-System.git)

**Local Location**: (Clone Directory)

## Source Code Structure
The solution consists of a **React Frontend** (`app/`) and a **FastAPI Backend** (`backend/`).

### 1. Frontend (`/app`)
Built with React, TypeScript, Tailwind CSS, and Shadcn UI.

*   `src/components/` - Reusable UI components (buttons, cards, layout).
*   `src/pages/` - Application pages (Dashboard, Cases, Analytics).
*   `src/lib/api.ts` - Axios configuration for backend communication.
*   `src/App.tsx` - Main application routing and context providers.

### 2. Backend (`/backend`)
Built with Python, FastAPI, SQLAlchemy, and Azure AI services.

*   `app/main.py` - Application entry point and CORS configuration.
*   `app/models.py` - Database models (User, Case, Message).
*   `app/routers/` - API endpoints (cases, users, analytics).
*   `app/services/` - Business logic (CTOS extraction, AI scoring, Email).
    *   `document_service.py` - Handles CTOS PDF parsing.
    *   `ai_explain.py` - Generates risk assessments via Azure OpenAI.
*   `alembic/` - Database migration scripts.

## Key Files for Review

| File Path | Description |
| :--- | :--- |
| `backend/app/services/document_service.py` | Logic for extracting data from CTOS PDFs. |
| `backend/app/services/ai_explain.py` | Prompt engineering for AI credit scoring. |
| `app/src/pages/CaseDetail.tsx` | Main UI for viewing case details, analysis, and handling **Override Decisions**. |
| `backend/app/models.py` | Database schema definition (including `CreditCase` and `User` models). |
| `backend/app/routers/cases.py` | API endpoints for case lifecycle (Create, Score, Submit, Approve/Override). |

## Complete File List
Below is a list of the primary source code files in the project.

### Frontend (`app/src`)
```text
src/
├── components/
│   ├── layout/
│   │   ├── Layout.tsx
│   │   ├── Sidebar.tsx
│   │   └── Topbar.tsx
│   ├── ui/ (Shadcn UI components)
│   ├── ui-custom/
│   │   ├── MetricCard.tsx
│   │   ├── RiskBadge.tsx
│   │   └── StatusBadge.tsx
│   ├── CaseChat.tsx
│   ├── CaseComments.tsx
│   ├── CompanyLoader.tsx
│   ├── ErrorBoundary.tsx
│   ├── GlobalChatWidget.tsx
│   ├── ProtectedRoute.tsx
│   └── theme-provider.tsx
├── hooks/
│   └── use-mobile.ts
├── lib/
│   ├── api.ts
│   └── utils.ts
├── pages/
│   ├── AdminDatabase.tsx
│   ├── AdminMessages.tsx
│   ├── AdminPanel.tsx
│   ├── Analytics.tsx
│   ├── CaseDetail.tsx
│   ├── Cases.tsx
│   ├── Dashboard.tsx
│   ├── Login.tsx
│   ├── ManagerDashboard.tsx
│   ├── OverrideMonitor.tsx
│   ├── PortfolioRisk.tsx
│   └── SystemPreferences.tsx
├── types/
│   └── index.ts
├── App.tsx
└── main.tsx
```

### Backend (`backend/app`)
```text
app/
├── routers/
│   ├── admin_db.py
│   ├── analytics.py
│   ├── cases.py
│   ├── messages.py
│   └── users.py
├── services/
│   ├── ai_chat_service.py
│   ├── ai_explain.py
│   ├── azure_doc_intel.py
│   ├── azure_openai.py
│   ├── azure_storage.py
│   ├── blob_service.py
│   ├── document_service.py
│   └── email.py
├── auth.py
├── database.py
├── main.py
├── models.py
├── schemas.py
└── utils.py
```

## How to Access Source Code
The complete source code is available in the project directory provided. To view the code:
1.  Open the folder in VS Code or any text editor.
2.  Navigate to the `app/` or `backend/` folders to explore the implementation.
