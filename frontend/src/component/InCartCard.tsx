import {
  Card,
  Image,
  Text,
  Badge,
  Button,
  Group,
  createStyles,
} from "@mantine/core";
import { JSXElementConstructor, ReactElement, ReactFragment, ReactPortal, useEffect, useState } from "react";

const useStyles = createStyles((theme) => ({
  wrapper: {
    width: "100%",
    //float: "right",
    display: "flex",
  },
}));

function InCartCard(props: { grocery: string }) {
  const { classes } = useStyles();

  async function removeGroceries(grocery:string){
    const response = await fetch(
      "http://localhost:5000/api/groceries?grocery="+grocery, { method: 'DELETE' }
    );
  };

  return (
    <div className={classes.wrapper}>
      <Card shadow="sm" padding="lg" radius="md" withBorder>
        <Card.Section>
          <Image
            src="https://th-thumbnailer.cdn-si-edu.com/qwdFU8TzPixEtFzRLC2V_Ezr2tw=/fit-in/1600x0/https%3A%2F%2Ftf-cmsv2-smithsonianmag-media.s3.amazonaws.com%2Ffiler%2Fd5%2F24%2Fd5243019-e0fc-4b3c-8cdb-48e22f38bff2%2Fistock-183380744.jpg"
            height={160}
            alt={props.grocery}
          />
        </Card.Section>

        <Group position="apart" mt="md" mb="xs">
          <Text weight={500}> {props.grocery}</Text>
        </Group>

        <Button variant="light" color="red" fullWidth mt="md" radius="md" onClick={()=> removeGroceries(props.grocery)}>
          Remove
        </Button>
      </Card>
    </div>
  );
}

export { InCartCard };
