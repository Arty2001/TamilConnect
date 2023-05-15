import data from "../data.json";
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
    //float: "right",
    display: "flex",
    flexDirection: "column",
  },
  addToCart: {},

  card: {},
}));

//let JsonString = data;

/*
data.forEach(obj => {
  Object.entries(obj).forEach(([key, value]) => {
      console.log(`${key} ${value}`);
  });
  */

export function ArticleCard(): JSX.Element {
  const { classes } = useStyles();
  return (
    <>
      {data.map((index, nb) => {
        return (
          <div className={classes.wrapper}>
            <Card
              shadow="sm"
              padding="lg"
              radius="md"
              withBorder
              className={classes.card}
            >
              <Card.Section>
                <Image src={index.link} height={160} alt="Item" />
              </Card.Section>

              <Group position="apart" mt="md" mb="xs">
                <Text weight={500}> {index.name}</Text>

                <Badge color="blue" variant="light">
                  {index.price}
                </Badge>
              </Group>

              <Button
                variant="light"
                color="green"
                fullWidth
                mt="md"
                radius="md"
                className={classes.addToCart}
              >
                Add To Cart
              </Button>
            </Card>
          </div>
        );
      })}
    </>
  );
}
