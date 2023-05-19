import React from 'react';
import { InputWithButton } from "../component/SearchBar";
import { createStyles } from "@mantine/core";
import { MapCard } from "../component/Map";

const useStyles = createStyles((theme) => ({}))



export function FindPage(){
  const {classes} = useStyles();

  return(
    <><InputWithButton>
    </InputWithButton><MapCard /></>
  );
  

}
export default FindPage;
