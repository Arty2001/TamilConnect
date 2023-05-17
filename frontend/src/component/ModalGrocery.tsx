import { useDisclosure } from "@mantine/hooks";
import { Modal, Group, Button, ScrollArea, Title } from "@mantine/core";

//import { Container } from "@mantine/core";
import { createStyles } from "@mantine/core";
import { ArticleCard } from "../component/GroceryItemCard";
import { InCartCard } from "../component/InCartCard";
import { useEffect, useState } from "react";
import { IconUpload } from "@tabler/icons-react";

const useStyles = createStyles((theme) => ({
  wrapper: {
    width: "90%",
    //float: "right",
    display: "flex",
    flexDirection: "column",
    backgroundColor: "#e7f5ff",
    boxShadow:
      "0 0.0625rem 0.1875rem rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 0 0.625rem 0.9375rem -0.3125rem, rgba(0, 0, 0, 0.04) 0 0.4375rem 0.4375rem -0.3125rem",
    borderRadius: "0.5rem",
    boxSizing: "border-box",
    padding: "1.25rem",
    transition: "1s",

    '&:hover': {
      boxShadow: "0px 10px 20px 20px rgba(0, 0, 0, 0.17)",
    }
  },
  rowOne: {
    display: "flex",
    gap: "1em",
  },

  rowTwo: {
    marginTop: "1em",
    display: "flex",
    gap: "1em",
  },
  Modal: {
    width: "1000px",
  },

  card: {
    textAlign: "left",
    transformOrigin: "50% 50%",
    transformStyle: "preserve-3d",
    minWidth: "595px",
    width: "90%",
    height: "520px",
    marginBottom: "10px",
  },
  titles: {
    color: "#3e3e42",
    fontSize: "32px",
    fontWeight: 800,
    letterSpacing: "-1px",
    marginBottom: "10px"
  },
  title: {
    color: "#228be6",
    fontSize: "16px",
  },
}));

export function ModalGrocery() {
  const [opened, { open, close }] = useDisclosure(false);
  const { classes } = useStyles();

  const [groceries, setGroceries] = useState([]);

  useEffect(() => {
    const fetchResto = async () => {
      const response = await fetch(
        "http://localhost:5000/api/groceries?cart=True"
      );
      const data = await response.json(); //json is the data shared among all
      setGroceries(data);
    };
    fetchResto();
  }, [groceries]);

  async function uploadFile(e: any) {
    const file = e.target.files[0];
    if (file != null) {
      const data = new FormData();
      data.append("file_from_react", file);

      let response = await fetch("/url_route", {
        method: "post",
        body: data,
      });
      let res = await response.json();

      if (res.status !== 1) {
        alert("Groceries Uploaded");
      }
    }
  }

  return (
    <>
      <Modal
        opened={opened}
        onClose={close}
        title="Grocery Items"
        scrollAreaComponent={ScrollArea.Autosize}
        className={classes.Modal}
        size="70%"
        centered
      >
        <ScrollArea h={375} type="auto" scrollbarSize={20}>
          <Group spacing={"lg"}>
              <ArticleCard />
          </Group>
        </ScrollArea>
        <input
          type="file"
          onChange={uploadFile}
          style={{ display: "none" }}
          id="contained-button-file"
        />
        <label htmlFor="contained-button-file">
        <Button
          variant="light"
          color="green"
          fullWidth
          mt="md"
          radius="md"
          leftIcon={<IconUpload/>}
          component="span"
        >
          Upload Receipt
        </Button>
        </label>
      </Modal>



      <div className={classes.wrapper}>
        <Title order={5} className={classes.title}>Groceries</Title>
        <Title order={1} className={classes.titles} >My Cart</Title>
        <ScrollArea h={300} type="auto" scrollbarSize={20}>
          <Group spacing={"lg"}>
            {groceries.map((grocery) => {
              return <InCartCard grocery={grocery} />
            })}
          </Group>
        </ScrollArea>
        <Button
          onClick={open}
          variant="light"
          color="green"
          fullWidth
          mt="md"
          radius="md"
        >
          Add Items
        </Button>
      </div>
    </>
  );
}
