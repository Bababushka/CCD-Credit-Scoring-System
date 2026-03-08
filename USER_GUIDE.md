# CashMeIfYouCan - User Guide

Welcome to the **CashMeIfYouCan** Credit Scoring System. This guide will help you navigate the application, manage credit cases, and utilize the AI-powered features effectively.

---

## 1. Getting Started

### Accessing the System
Open your web browser and navigate to the application URL (typically `http://localhost:5173` for local development).

### Login Credentials
Use the following default credentials to log in based on your role:

| Role | Username | Password | Access Level |
| :--- | :--- | :--- | :--- |
| **Officer** | `officer` | `123456` | Create & Manage Cases, Upload Documents, Extract Data |
| **Finance Manager** | `finance` | `123456` | View Cases, Approve/Reject Credit Limits |
| **Admin** | `admin` | `123456` | System Administration, User Management |

---

## 2. Key Features

-   **Dashboard**: A centralized view of all credit cases with status indicators (Draft, Pending, Approved, etc.).
-   **Case Management**: Create, update, and track credit applications for companies.
-   **CTOS Integration**: Upload CTOS PDF reports and automatically extract financial and director data.
-   **AI Credit Scoring**: Automatically generate a credit score and risk assessment based on extracted data.
-   **Notifications**: Receive email and desktop notifications for case updates (configurable).
-   **Role-Based Workflows**: Distinct permissions for Officers (submission) and Managers (approval).

---

## 3. How to Use the Solution

### Step 1: Dashboard Overview
Upon logging in, you will see the **Dashboard**.
-   **Metrics**: View total active cases, pending approvals, and risk distribution.
-   **Recent Cases**: A list of the most recently updated cases.
-   Click on any case ID or Company Name to view details.

### Step 2: Creating a New Case (Officer Only)
1.  Navigate to the **Cases** page via the sidebar.
2.  Click the **"New Case"** button.
3.  Enter the **Company Name** and **Reference Number** (e.g., `REF-2024-001`).
4.  Click **"Create Case"**. The case will be created in `DRAFT` status.

### Step 3: Uploading & Extracting Data
1.  Open the newly created case.
2.  Scroll down to the **CTOS Documentation** section.
3.  Click **"Choose File"** and select a CTOS PDF report.
4.  Click **"Upload CTOS"**.
5.  Once uploaded, click **"Extract Data"**.
    -   *Note: The system will parse the PDF and populate the "Extracted Data Preview" box with financial and CCRIS details.*

### Step 4: Generating AI Analysis
1.  After extracting data, locate the **AI Risk Assessment** card.
2.  Click **"Generate AI Assessment"**.
3.  The AI will analyze the extracted data and provide:
    -   **Confidence Score**: How reliable the assessment is.
    -   **Risk Explanation**: A summary of the company's financial health.
    -   **Key Risk Flags**: Specific issues (e.g., "High Utilisation", "Blacklist Match").
    -   **Recommended Action**: (e.g., "Approve with Conditions").

### Step 5: Approval Process
1.  **Officer**: Once the analysis is complete, you can submit the case for approval (if workflow is enabled) or set a proposed limit.
2.  **Finance Manager**: Log in as `finance`.
    -   Review the case details, extracted data, and AI scores.
    -   Approve or Reject the proposed credit limit.

---

## 4. System Preferences

You can customize your notification settings:
1.  Click on your **Profile/Avatar** in the top right corner.
2.  Select **Settings** or navigate to the **System Preferences** page.
3.  Toggle **Email Notifications** or **Desktop Notifications** as desired.
    -   *Note: Desktop notifications require browser permission.*

---

## 5. Troubleshooting

-   **"Method Not Allowed" Error**: Ensure you are using the correct buttons for case creation.
-   **Extraction Failed**: Ensure the uploaded file is a valid PDF. If using the mock mode, ensure the system is running correctly.
-   **Empty Extraction Preview**: Click "Extract Data" again to refresh the structured data parsing.

---

*© 2026 Chin Hin Group - CashMeIfYouCan*
