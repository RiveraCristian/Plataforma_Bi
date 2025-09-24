import { Card, Group, Text } from "@mantine/core";
import { IconChartBar } from "@tabler/icons-react";

interface WidgetProps {
  title: string;
  description: string;
}

function Widget({ title, description }: WidgetProps) {
  return (
    <Card shadow="sm" padding="lg" radius="md" withBorder>
      <Group align="center" mb="sm">
        <IconChartBar size={20} />
        <Text fw={600}>{title}</Text>
      </Group>
      <Text size="sm" c="dimmed">
        {description}
      </Text>
    </Card>
  );
}

export default Widget;
