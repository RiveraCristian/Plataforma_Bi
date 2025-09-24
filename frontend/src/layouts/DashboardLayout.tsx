import { ReactNode } from "react";
import { Card } from "@mantine/core";

interface DashboardLayoutProps {
  title: string;
  children: ReactNode;
}

function DashboardLayout({ title, children }: DashboardLayoutProps) {
  return (
    <Card withBorder shadow="sm" padding="md">
      <Card.Section inheritPadding py="md">
        <strong>{title}</strong>
      </Card.Section>
      {children}
    </Card>
  );
}

export default DashboardLayout;
