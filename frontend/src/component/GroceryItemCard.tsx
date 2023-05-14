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
  },
}));

//let JsonString = data;
//console.log(JsonString);

export function ArticleCard() {
  const { classes } = useStyles();
  let JsonString = data;

  return (
    <div className={classes.wrapper}>
      {data.map((index, key) => {
        return (
          <Card shadow="sm" padding="lg" radius="md" withBorder>
            <Card.Section>
              <Image
                src={
                  "https://hips.hearstapps.com/hmg-prod/images/2024-lamborghini-revuelto-127-641a1d518802b.jpg?crop=0.769xw:0.770xh;0.104xw,0.106xh&resize=1200:*"
                }
                height={160}
                alt="Item"
              />
            </Card.Section>

            <Group position="apart" mt="md" mb="xs">
              {data.map((index, key) => {
                return (
                  <Text weight={500} key={key}>
                    {" "}
                    {index.name}
                  </Text>
                );
              })}
              <Badge color="blue" variant="light">
                8.99
              </Badge>
            </Group>

            <Button variant="light" color="green" fullWidth mt="md" radius="md">
              Add To Cart
            </Button>
          </Card>
        );
      })}
    </div>
  );
}
