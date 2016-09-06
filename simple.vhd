library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity simple is
  port (
    in_port, in_port2 : in std_logic;
    out_port, out_port2 : out std_logic
  );
end simple;

architecture Behavioral of simple is

begin
  out_port <= in_port;
  out_port2 <= in_port2;
end Behavioral;
