import { create } from "zustand";

import type { DashboardDefinition } from "../types/dashboard";

interface DashboardState {
  dashboards: DashboardDefinition[];
  setDashboards: (dashboards: DashboardDefinition[]) => void;
}

export const useDashboardStore = create<DashboardState>((set) => ({
  dashboards: [],
  setDashboards: (dashboards) => set({ dashboards })
}));
