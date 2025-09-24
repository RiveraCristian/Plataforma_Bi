import { useEffect } from "react";
import { Card, Grid, Group, Image, Text, Title } from "@mantine/core";

import { fetchDashboards } from "../services/api";
import type { DashboardDefinition } from "../types/dashboard";
import { useDashboardStore } from "../store/dashboardStore";

function DashboardListPage() {
  const { dashboards, setDashboards } = useDashboardStore();

  useEffect(() => {
    fetchDashboards()
      .then((data) => setDashboards(data))
      .catch(() => {
        setDashboards([
          {
            id: 1,
            name: "Ventas regionales",
            owner_id: 1,
            layout_json: {},
            description: "Seguimiento de ventas por región"
          },
          {
            id: 2,
            name: "Marketing digital",
            owner_id: 1,
            layout_json: {},
            description: "Campañas y conversiones"
          }
        ]);
      });
  }, [setDashboards]);

  return (
    <section>
      <Title order={2} mb="md">
        Dashboards
      </Title>
      <Grid>
        {dashboards.map((dashboard) => (
          <Grid.Col key={dashboard.id} span={{ base: 12, sm: 6, md: 4 }}>
            <Card shadow="sm" padding="lg" radius="md" withBorder>
              <Card.Section>
                <Image src="https://placehold.co/600x400?text=Dashboard" alt={dashboard.name} height={140} />
              </Card.Section>
              <Group justify="space-between" mt="md">
                <Text fw={600}>{dashboard.name}</Text>
              </Group>
              <Text size="sm" c="dimmed">
                {dashboard.description ?? "Dashboard sin descripción"}
              </Text>
            </Card>
          </Grid.Col>
        ))}
      </Grid>
    </section>
  );
}

export default DashboardListPage;
