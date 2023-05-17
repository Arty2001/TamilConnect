import {
  Card,
  Image,
  Text,
  Badge,
  Button,
  Group,
  createStyles,
} from "@mantine/core";

const useStyles = createStyles((theme) => ({
  wrapper: {
    width: "100%",
    float: "right",
    display: "flex",
    height: "100%",
  },
}));

function DaCard() {
  const { classes } = useStyles();

  return (
    <div className={classes.wrapper} >
      <Card shadow="sm" padding="lg" radius="md" withBorder>
        <Card.Section>
          <Image
            src="https://cheapandcheerfulcooking.com/wp-content/uploads/2023/02/vegan-kottu-roti-1.jpg"
            height={160}
            alt="Khotu Rotti"
          />
        </Card.Section>

        <Group position="apart" mt="md" mb="xs">
          <Text weight={500}> Kothu Rotti</Text>
          <Badge color="green" variant="light">
            Trending
          </Badge>
        </Group>

        <Text size="sm" color="dimmed" lineClamp={3}>
          Kottu roti is a Sri Lankan dish consisting of chopped roti, a meat
          curry dish of choice, along with scrambled egg, onions, and chillies.
        </Text>

        <Button variant="light" color="blue" fullWidth mt="md" radius="md">
          View recipe
        </Button>
      </Card>
    </div>
  );
}

function DaCard2() {
  const { classes } = useStyles();

  return (
    <div className={classes.wrapper}>
      <Card shadow="sm" padding="lg" radius="md" withBorder>
        <Card.Section>
          <Image
            src="data:image/jpeg;base64,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"
            height={160}
            alt="dosai"
          />
        </Card.Section>

        <Group position="apart" mt="md" mb="xs">
          <Text weight={500}> Dosai</Text>
          <Badge color="green" variant="light">
            Trending
          </Badge>
        </Group>

        <Text size="sm" color="dimmed" lineClamp={3}>
          A dosai is made from a fermented batter of ground black lentils and
          rice. Dosas are served hot, often with chutney and sambar.
        </Text>

        <Button variant="light" color="blue" fullWidth mt="md" radius="md">
          View recipe
        </Button>
      </Card>
    </div>
  );
}

function DaCard3() {
  const { classes } = useStyles();

  return (
    <div className={classes.wrapper}>
      <Card shadow="sm" padding="lg" radius="md" withBorder>
        <Card.Section>
          <Image
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcROuM67QH2Q_Po8I7KB3layZOqXCfFHQB3zhw&usqp=CAU"
            height={160}
            alt="mutton curry"
          />
        </Card.Section>

        <Group position="apart" mt="md" mb="xs">
          <Text weight={500}> Mutton Curry</Text>
          <Badge color="green" variant="light">
            Trending
          </Badge>
        </Group>

        <Text size="sm" color="dimmed" lineClamp={3}>
          Mutton curry is a dish that is prepared from goat meat and vegetables
          in spicy onion tomato gravy.
        </Text>

        <Button variant="light" color="blue" fullWidth mt="md" radius="md">
          View recipe
        </Button>
      </Card>
    </div>
  );
}

function DaCard4() {
  const { classes } = useStyles();

  return (
    <div className={classes.wrapper}>
      <Card shadow="sm" padding="lg" radius="md" withBorder>
        <Card.Section>
          <Image
            src="https://revisfoodography.com/wp-content/uploads/2017/01/idiyappam-main.jpg"
            height={160}
            alt="idiyappam"
          />
        </Card.Section>

        <Group position="apart" mt="md" mb="xs">
          <Text weight={500}>idiyappam</Text>
          <Badge color="green" variant="light">
            Trending
          </Badge>
        </Group>

        <Text size="sm" color="dimmed" lineClamp={3}>
          Idiyappam consists of rice flour pressed into noodles, laid into a
          flat disc-like shape and steamed.
        </Text>

        <Button variant="light" color="blue" fullWidth mt="md" radius="md">
          View recipe
        </Button>
      </Card>
    </div>
  );
}

export { DaCard, DaCard2, DaCard3, DaCard4 };
