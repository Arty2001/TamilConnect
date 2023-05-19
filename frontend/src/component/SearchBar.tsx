import { IconSearch, IconArrowRight, IconArrowLeft } from '@tabler/icons-react';
import { TextInput, TextInputProps, Stack, ActionIcon, useMantineTheme } from '@mantine/core';


export function InputWithButton(props: TextInputProps) {
    const theme = useMantineTheme();
  
    return (
      <Stack align="center" h ={100} >
      <div style={{width: '500px'}}>
      <TextInput
        icon={<IconSearch size="1.1rem" stroke={1.5} />}
        radius="xl"
        size="md"
        rightSection={
          <ActionIcon size={32} radius="xl" color={theme.primaryColor} variant="filled">
            {theme.dir === 'ltr' ? (
              <IconArrowRight size="1.1rem" stroke={1.5} />
            ) : (
              <IconArrowLeft size="1.1rem" stroke={1.5} />
            )}
          </ActionIcon>
        }
        placeholder="Please enter your address"
        rightSectionWidth={42}
        {...props}
      />
      </div>
      </Stack>
    );
  }
  export default InputWithButton