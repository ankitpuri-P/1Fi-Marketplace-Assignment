# 1Fi SDE Intern Assignment: Marketplace Feature

![React Native](https://img.shields.io/badge/React_Native-Expo-61DAFB?style=flat-square&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)

## Overview
This repository contains the implementation of the **1Fi Marketplace** feature, built as an extension to the existing Shop page within the 1Fi mobile app. The objective was to design a responsive, native-feeling marketplace that perfectly aligns with 1Fi's existing design system, while dynamically handling product data without hardcoding.

## Features at a Glance
- Product listing with images, pricing, and variant options
- Variant selection (e.g., color) with live UI updates to image and price
- EMI plan comparison across multiple tiers, with tier selection
- Persistent "Proceed" CTA
- Fully dynamic data — zero hardcoded product/EMI values in the UI layer

## Architecture & Tech Stack
- **Frontend:** React Native (Expo), TypeScript, React Navigation (Bottom Tabs & Native Stack)
- **Backend API:** Python, FastAPI, Uvicorn
- **State Management:** React Hooks (`useState`, `useEffect`)

## Prerequisites
- **Node.js** ≥ 18.x and npm
- **Python** ≥ 3.9 and pip
- **Expo Go** app on your physical test device (available on the iOS App Store and Google Play) — only needed if you're testing on a physical device rather than a simulator/emulator
- Git

## Project Structure
*(Illustrative — adjust paths to match your actual repository layout.)*

```
.
├── main.py                   # FastAPI mock backend (product & EMI data)
├── 1FiMarketplace/            # Expo React Native app
│   ├── src/
│   │   ├── components/
│   │   │   ├── SegmentedToggle.tsx
│   │   │   └── ProductCard.tsx
│   │   ├── screens/
│   │   │   └── ProductDetailScreen.tsx
│   │   ├── theme/
│   │   │   └── tokens.ts
│   │   └── types/
│   │       └── types.ts
│   ├── App.tsx
│   └── package.json
└── README.md
```

## Fulfilling the Evaluation Criteria

### 1. UI/UX Consistency & Product Understanding
- **Design System Integration:** Extracted and implemented a centralized `tokens.ts` file covering 1Fi's exact color palette (Primary `#6B4EFF`), typography weights, border radii, and soft shadow elevations.
- **Component Architecture:** Built isolated, reusable UI components (`SegmentedToggle.tsx`, `ProductCard.tsx`) to mimic the existing application structure.
- **Navigation:** Implemented a persistent Bottom Tab navigator mapping to the core app sections, with a secondary Stack Navigator to handle seamless transitions into the Product Detail view.

### 2. Data & API Implementation (Zero Hardcoding)
- **Mock Backend Service:** Engineered a local FastAPI Python server to deliver structured JSON data, strictly adhering to the requirement to avoid hardcoding product/EMI data into UI components.
- **Type Safety:** Defined strict TypeScript interfaces (`types.ts`) mapping exactly to the backend schema to ensure predictable data flow and eliminate runtime errors.
- **Dynamic Variant Rendering:** Engineered the Product Detail screen to actively listen to state changes, dynamically updating the hero image and EMI pricing tables based on the user's selected color variant and EMI tier.

### 3. Attention to Detail & Engineering Quality
- **Loading & Error Handling:** Implemented `ActivityIndicator` loading states during asynchronous API fetches, preventing blank UI renders. Added fallback `defaultSource` image URIs for network resilience.
- **Performance:** Restricted the API fetch execution to trigger only when the user explicitly toggles to the "1Fi Marketplace" tab, preventing unnecessary network payloads.
- **Localization:** Utilized native `Intl.NumberFormat` for accurate Indian Rupee (INR) currency formatting.

## Setup & Run Instructions

### 1. Start the Backend API
Navigate to the root directory and start the server:
```bash
pip install fastapi uvicorn
uvicorn main:app --host 0.0.0.0 --reload
```

### 2. Start the Mobile Frontend (Expo Go)
The frontend is built with React Native (Expo). You can test the app on an Android Emulator, iOS Simulator, or directly on a physical device using the Expo Go app.

Ensure your testing device or emulator is on the same Wi-Fi network as your host machine, open a new terminal, and run:
```bash
cd 1FiMarketplace
npm install
npx expo start --clear
```

Once the server starts, scan the generated QR code with the Expo Go app (Android) or the native Camera app (iOS) to launch the application.

> **Note:** If you're testing on a physical device, `localhost` in your app's API calls won't reach a server running on your computer. Find your machine's local IP address (`ipconfig` on Windows, `ipconfig getifaddr en0` on macOS) and use that instead — e.g. `http://192.168.1.5:8000` — wherever the API base URL is configured.

## Troubleshooting
- **CORS errors in the app logs** → add `CORSMiddleware` to `main.py`:
```python
  from fastapi.middleware.cors import CORSMiddleware
  app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
```
- **Port 8000 already in use** → stop the conflicting process, or run on another port with `uvicorn main:app --host 0.0.0.0 --port 8001 --reload` and update the API base URL accordingly.
- **Expo Go shows an SDK version mismatch** → update the Expo Go app on your device, or run `npx expo install --fix`.

---

*Developed by Ankit Puri for the 1Fi SDE Intern Evaluation.*
