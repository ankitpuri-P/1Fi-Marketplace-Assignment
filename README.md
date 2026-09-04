# 1Fi SDE Intern Assignment: Marketplace Feature

## Overview
This repository contains the implementation of the **1Fi Marketplace** feature, built as an extension to the existing Shop page within the 1Fi mobile app. The objective was to design a responsive, native-feeling marketplace that perfectly aligns with 1Fi's existing design system, while dynamically handling product data without hardcoding.

## Architecture & Tech Stack
* **Frontend:** React Native (Expo), TypeScript, React Navigation (Bottom Tabs & Native Stack)
* **Backend API:** Python, FastAPI, Uvicorn
* **State Management:** React Hooks (`useState`, `useEffect`)

## Fulfilling the Evaluation Criteria

### 1. UI/UX Consistency & Product Understanding
* **Design System Integration:** Extracted and implemented a centralized `tokens.ts` file covering 1Fi’s exact color palette (Primary `#6B4EFF`), typography weights, border radii, and soft shadow elevations.
* **Component Architecture:** Built isolated, reusable UI components (`SegmentedToggle.tsx`, `ProductCard.tsx`) to mimic the existing application structure. 
* **Navigation:** Implemented a persistent Bottom Tab navigator mapping to the core app sections, with a secondary Stack Navigator to handle seamless transitions into the Product Detail view.

### 2. Data & API Implementation (Zero Hardcoding)
* **Mock Backend Service:** Engineered a local FastAPI Python server to deliver structured JSON data, strictly adhering to the requirement to avoid hardcoding product/EMI data into UI components.
* **Type Safety:** Defined strict TypeScript interfaces (`types.ts`) mapping exactly to the backend schema to ensure predictable data flow and eliminate runtime errors.
* **Dynamic Variant Rendering:** Engineered the Product Detail screen to actively listen to state changes, dynamically updating the hero image and EMI pricing tables based on the user's selected color variant and EMI tier.

### 3. Attention to Detail & Engineering Quality
* **Loading & Error Handling:** Implemented `ActivityIndicator` loading states during asynchronous API fetches, preventing blank UI renders. Added fallback `defaultSource` image URIs for network resilience.
* **Performance:** Restricted the API fetch execution to trigger only when the user explicitly toggles to the "1Fi Marketplace" tab, preventing unnecessary network payloads.
* **Localization:** Utilized native `Intl.NumberFormat` for accurate Indian Rupee (INR) currency formatting.

## Setup & Run Instructions

### 1. Start the Backend API
Navigate to the root directory and start the server:
```bash
pip install fastapi uvicorn
uvicorn main:app --host 0.0.0.0 --reload
