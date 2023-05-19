import React, { useEffect, useRef } from 'react';
import { AspectRatio } from '@mantine/core';
import { Input, Tooltip } from '@mantine/core';
import { TextInput, TextInputProps, ActionIcon, useMantineTheme } from '@mantine/core';
import { IconHeart } from '@tabler/icons-react';
import { Card, Image, Text, Group, Badge, Button, createStyles, Stack, rem,} from '@mantine/core';
import {BsThreeDots} from '@tabler/icons-react';
declare global {
  interface Window {
    google: any;
  }
}

interface MapProps {
  locations: { lat: number; lng: number; }[];
}





const useStyles = createStyles((theme) => ({
  card: {
    width: "90%" , 
  }
}));


export function MapCard() {
  const { classes, theme } = useStyles();

  return (
    



    <Card shadow="lg" padding="lg" radius="md" withBorder className = {classes.card}>
        <Group>
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d20368.692398824787!2d-73.61989659453465!3d45.56004934874796!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cc91fe4a7280da3%3A0x57e796589086150e!2sMarch%C3%A9%20Murugan!5e0!3m2!1sen!2sca!4v1684264915854!5m2!1sen!2sca" width="300" height="300" loading="lazy" ></iframe> 
          <Stack justify="flex-start" h={300}>
            <Text fw={700} fz="lg">Marche Murugan</Text>
            <Group>
              <Stack align = "center"> 
                <Text fz="lg">Sunday</Text>
                <Text fz="lg">9:00-20:00</Text>
              </Stack >
              <Stack align = "center"> 
                <Text fz="lg">Monday</Text>
                <Text fz="lg">9:00-20:00</Text>
              </Stack>
              <Stack align = "center"> 
                <Text fz="lg">Tuesday</Text>
                <Text fz="lg">9:00-20:00</Text>
              </Stack>
              <Stack align = "center"> 
                <Text fz="lg">Wednesday</Text>
                <Text fz="lg">9:00-20:00</Text>
              </Stack>
              <Stack align = "center"> 
                <Text fz="lg">Thursday</Text>
                <Text fz="lg">9:00-20:00</Text>
              </Stack>
              <Stack align = "center"> 
                <Text fz="lg">Friday</Text>
                <Text fz="lg">9:00-20:00</Text>
              </Stack>
              <Stack align = "center"> 
                <Text fz="lg">Saturday</Text>
                <Text fz="lg">9:00-20:00</Text>
              </Stack>
            </Group>
            <Group>
          <Badge color ="green" radius="md">Artichoke</Badge>
          <Badge color ="green" radius="md">Asparagus</Badge>
          <Badge color ="green" radius="md">Eggplant</Badge>
          <Badge color ="green" radius="md">Avocado</Badge>
          <Badge color ="green" radius="md">Beet</Badge>
          <Badge color ="green" radius="md">Bok Choy</Badge>
          <Badge color ="green" radius="md">Broccoli</Badge>
          <Badge color ="green" radius="md">Brussels Sprout</Badge>
          <BsThreeDots size = {24} />
          </Group>

          
          </Stack>
          
        </Group>
    </Card>


  );
}


export default MapCard;