# CashMeIfYouCan - User Guide

Welcome to the **CashMeIfYouCan** Credit Scoring System. This guide will help you navigate the application, manage credit cases, and utilize the AI-powered features effectively.

---

## 1. Getting Started

### Accessing the System
Open your web browser and navigate to the application URL (typically `http://localhost:3000` for local development).

### Login Credentials
Use the following default credentials to log in based on your role.
**Note: The password for all users is `password`.**

| Role | Username | Password | Access Level |
| :--- | :--- | :--- | :--- |
| **Officer** | `analyst` | `password` | Create & Manage Cases, Upload Documents, Extract Data, Score Cases |
| **Finance Manager** | `manager` | `password` | View Cases, Approve/Reject Credit Limits, Override Decisions |
| **Admin** | `admin` | `password` | System Administration, User Management, Archiving |

*(Note: Legacy users `officer` and `finance` may also exist with password `123456` or `password`, but `analyst` and `manager` are the primary test accounts).*

---

## 2. Key Features

-   **Dashboard**: A centralized view of all credit cases with status indicators (Draft, Pending, Approved, etc.).
-   **Case Management**: Create, update, and track credit applications for companies.
-   **CTOS Integration**: Upload CTOS PDF reports and automatically extract financial and director data.
-   **AI Credit Scoring**: Automatically generate a credit score and risk assessment based on extracted data.
-   **Override Decision**: Finance Managers can override AI-suggested limits with mandatory justification for accountability.
-   **Notifications**: Receive email and desktop notifications for case updates.

---

## 3. How to Use the Solution

### Step 1: Dashboard Overview
Upon logging in, you will see the **Dashboard**.
-   **Metrics**: View total active cases, pending approvals, and risk distribution.
-   **Recent Cases**: A list of the most recently updated cases.
-   Click on any case ID or Company Name to view details.

### Step 2: Creating a New Case (Officer Only)
1.  Log in as **Officer** (`analyst`).
2.  Navigate to the **Cases** page via the sidebar.
3.  Click the **"New Case"** button.
4.  Enter the **Company Name** and **Reference Number** (e.g., `REF-2024-001`).
5.  Click **"Create Case"**. The case will be created in `DRAFT` status.

### Step 3: Uploading & Extracting Data
1.  Open the newly created case.
2.  Scroll down to the **CTOS Documentation** section.
3.  Click **"Choose File"** and select a CTOS PDF report.
4.  Click **"Upload CTOS"**.
5.  Once uploaded, click **"Extract Data"**.
    -   *The system will parse the PDF and populate the "Extracted Data Preview" box with financial and CCRIS details.*

### Step 4: Generating AI Analysis & Scoring
1.  After extraction, locate the **AI Risk Assessment** card.
2.  Click **"Generate AI Assessment"** to get a risk explanation and key flags.
3.  In the **Risk Summary** card (right sidebar), click **"Calculate Score"**.
    -   The system will calculate a Credit Score (0-100) and a Risk Grade (1-5).
    -   A **Suggested Limit** will be generated based on the score.

### Step 5: Submission
1.  Review the **Suggested Limit**.
2.  (Optional) Click the **Edit** icon next to **Proposed Limit** to adjust the amount before submission.
3.  Click **"Submit for Approval"**. The case status changes to `SUBMITTED_FOR_APPROVAL`.

### Step 6: Approval & Override (Finance Manager Only)
1.  Log in as **Finance Manager** (`manager`).
2.  Navigate to the **Cases** page or Dashboard to find pending cases.
3.  Open the case details.
4.  Review the extracted data, AI analysis, and score.
5.  **To Approve as Proposed**:
    -   Click **"Approve & Override"**.
    -   Ensure the "Override Decision" toggle is **OFF**.
    -   Click **"Confirm Approval"**.
6.  **To Override the Decision**:
    -   Click **"Approve & Override"**.
    -   Toggle **"Override Decision"** to **ON**.
    -   Enter the new **Approved Limit**.
    -   Select a **Reason Code** (e.g., "Market Conditions", "Strategic Client").
    -   Enter a **Justification** explanation.
    -   Click **"Confirm Override"**.

### Step 7: Post-Decision
-   **Approved**: The case is closed with a Final Credit Limit.
-   **Rejected**: The case is closed as Rejected.
-   **Returned**: The case is sent back to the Officer for rework (e.g., missing documents).

---

## 4. Troubleshooting

-   **"Method Not Allowed" Error**: Ensure you are using the correct buttons for case creation.
-   **Extraction Failed**: Ensure the uploaded file is a valid PDF.
-   **Login Failed**: Verify you are using `analyst` / `manager` with password `password`.

---

*© 2026 Chin Hin Group - CashMeIfYouCan*
