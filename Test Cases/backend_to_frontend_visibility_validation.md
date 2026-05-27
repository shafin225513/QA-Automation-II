# Test Case - Backend-to-Frontend Visibility Validation

---

# Test Case ID
TC-E2E-001

---

# Test Title
Verify that a product created through backend API is successfully visible in the frontend user interface.

---

# Test Type
End-to-End (E2E) Hybrid Testing

---

# Objective

Validate complete backend-to-frontend data flow by confirming that product data created through API integration appears correctly in the web application UI.

This test ensures synchronization between:
- Backend API
- Database/Data Layer
- Frontend UI Rendering

---

# Automation Scope

This test combines:
- API Testing
- UI Automation Testing
- Integration Validation

---

# Tools & Technologies

| Tool | Purpose |
|---|---|
| Python | Automation scripting |
| Playwright | UI automation |
| Pytest | Test execution |
| Requests/API Client | Backend API communication |

---

# Preconditions

- Backend API server running
- Frontend application accessible
- Product API endpoint available
- Browser environment configured
- Test environment database accessible

---

# Test Flow

```text
API Product Creation
        ↓
Frontend Navigation
        ↓
UI Interaction
        ↓
DOM Validation
        ↓
Visibility Verification
```

---

# Test Steps

| Step | Action | Logic / Component |
|---|---|---|
| 1 | Create test product through API | `ProductClient.create_product()` |
| 2 | Open product dashboard page | `ProductPage.navigate()` |
| 3 | Navigate through UI flow/menu | `ProductPage.go_to_guide()` |
| 4 | Validate product visibility in UI | `ProductPage.verify_product_visible()` |

---

# Test Data

| Field | Value |
|---|---|
| Product Name | Portfolio Camera |
| Product Source | Backend API |
| Verification Area | Product Dashboard UI |

---

# Detailed Execution Steps

## Step 1 - Seed Backend Data

Create a new product named:
```text
Portfolio Camera
```

through backend API request using:
```python
ProductClient.create_product()
```

### Expected Result
API should successfully create the product and return successful response.

---

## Step 2 - Navigate to Product Dashboard

Open frontend application and navigate to product listing/dashboard page using:
```python
ProductPage.navigate()
```

### Expected Result
Product listing page should load successfully.

---

## Step 3 - Perform UI Navigation

Interact with navigation menu and required UI flow using:
```python
ProductPage.go_to_guide()
```

### Expected Result
Application should navigate to target product display section.

---

## Step 4 - Validate Product Visibility

Search frontend DOM for:
```text
Portfolio Camera
```

using:
```python
ProductPage.verify_product_visible()
```

### Expected Result
Product created through API should appear visibly in frontend UI.

---

# Expected Final Result

The product created through backend API should successfully render and appear in the frontend dashboard interface.

---

# Actual Result

Product successfully appeared in frontend UI after API creation.

---

# Status

PASS

---

# Validation Areas Covered

- API functionality
- Backend integration
- Data persistence
- Frontend rendering
- UI synchronization
- End-to-End system behavior

---

# Assertions Performed

- API response validation
- Successful page navigation
- DOM visibility assertion
- Product title verification

---

# Failure Conditions

Test should fail if:
- API creation fails
- Product not persisted
- Frontend does not update
- DOM element missing
- Navigation errors occur

---

# Importance of This Test

This is a critical hybrid QA validation because it verifies:
- Backend and frontend integration
- Real system workflow
- Cross-layer application consistency

Unlike isolated UI tests, this scenario validates actual business flow behavior across multiple system components.

---

# QA Concepts Demonstrated

- End-to-End Testing
- Integration Testing
- API Testing
- UI Automation
- Data Validation
- Backend-to-Frontend Synchronization
- Hybrid QA Workflow
