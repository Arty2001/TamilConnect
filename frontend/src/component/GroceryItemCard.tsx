import { useEffect, useState } from "react";
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

  const [groceries, setGroceries] = useState([]);

  useEffect(() => {
    const fetchResto = async () => {
      const response = await fetch(
        "http://localhost:5000/api/groceries?cart=False"
      );
      const data = await response.json(); //json is the data shared among all
      setGroceries(data);
    };
    fetchResto();
  }, [groceries]);

  async function addGroceries(grocery: string) {
    const response = await fetch(
      "http://localhost:5000/api/groceries?grocery=" + grocery, { method: 'POST' }
    );
  };
  
  return (
    <>
      {groceries.map((grocery) => {
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
                <Image src={""} height={160} alt="Item" />
              </Card.Section>

              <Group position="apart" mt="md" mb="xs">
                <Text weight={500}> {grocery}</Text>

                <Badge color="blue" variant="light">
                  {grocery}
                </Badge>
              </Group>

              <Button
                variant="light"
                color="green"
                fullWidth
                mt="md"
                radius="md"
                className={classes.addToCart}
                onClick={()=>addGroceries(grocery)}
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
