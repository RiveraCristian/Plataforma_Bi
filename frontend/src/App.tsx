import { AppShell, Container, Group, Title } from "@mantine/core";

import DashboardListPage from "./pages/DashboardListPage";
import DashboardEditorPage from "./pages/DashboardEditorPage";
import MetricEditor from "./components/MetricEditor";
import FilterPanel from "./components/FilterPanel";

function App() {
  return (
    <AppShell
      header={{ height: 60 }}
      padding="md"
      styles={{ main: { backgroundColor: "#f6f8fb" } }}
    >
      <AppShell.Header>
        <Group h="100%" px="md">
          <Title order={3}>Plataforma BI</Title>
        </Group>
      </AppShell.Header>
      <AppShell.Main>
        <Container size="xl">
          <DashboardListPage />
          <DashboardEditorPage />
          <Group align="flex-start" mt="xl" grow>
            <MetricEditor />
            <FilterPanel />
          </Group>
        </Container>
      </AppShell.Main>
    </AppShell>
  );
}

export default App;
