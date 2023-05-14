import { useDisclosure } from "@mantine/hooks";
import { Modal, Group, Button, ScrollArea } from "@mantine/core";

//import { Container } from "@mantine/core";
import { createStyles } from "@mantine/core";
import { ArticleCard } from "../component/GroceryItemCard";
import { InCartCard } from "../component/InCartCard";

const useStyles = createStyles((theme) => ({
  wrapper: {
    width: "100%",
    //float: "right",
    display: "flex",
    flexDirection: "column",
    backgroundColor: "#e7f5ff",
    boxShadow:
      "0 0.0625rem 0.1875rem rgba(0, 0, 0, 0.05), rgba(0, 0, 0, 0.05) 0 0.625rem 0.9375rem -0.3125rem, rgba(0, 0, 0, 0.04) 0 0.4375rem 0.4375rem -0.3125rem",
    borderRadius: "0.5rem",
    boxSizing: "border-box",
    padding: "1.25rem",
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
}));

export function ModalGrocery() {
  const [opened, { open, close }] = useDisclosure(false);
  const { classes } = useStyles();

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
        <ScrollArea h={400} type="auto" scrollbarSize={20}>
          <div className={classes.wrapper}>
            <div className={classes.rowOne}>
              <ArticleCard />
              <ArticleCard />
              <ArticleCard />
              <ArticleCard />
              <ArticleCard />
              <ArticleCard />
            </div>
            <div className={classes.rowTwo}>
              <ArticleCard />
              <ArticleCard />
              <ArticleCard />
              <ArticleCard />
              <ArticleCard />
              <ArticleCard />
            </div>
          </div>
        </ScrollArea>
      </Modal>

      <div className={classes.wrapper}>
        <ScrollArea h={400} type="auto" scrollbarSize={20}>
          <div className={classes.rowOne}>
            <InCartCard />
            <InCartCard />
            <InCartCard />
            <InCartCard />
            <InCartCard />
            <InCartCard />
          </div>
          <div className={classes.rowTwo}>
            <InCartCard />
            <InCartCard />
            <InCartCard />
            <InCartCard />
            <InCartCard />
            <InCartCard />
          </div>
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
