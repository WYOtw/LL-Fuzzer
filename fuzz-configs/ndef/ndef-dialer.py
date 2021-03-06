"""
    Fuzzing template for the NDEF dialer

    (c) 2015 Massachusetts Institute of Technology
"""
# This is very similar to ndef-string.py -- may want to combine?
# Looks like we may not be able to - fuzzing the type block can
# mess up nfcpy's parsing of the raw data

# define grammar for NDEF Record
s_initialize("NDEF Dialer")

# NDEF record header
s_byte(0xd1, format="binary", name="header", full_range=True, fuzzable=False)

# NDEF type length field, tied to 'type block'
s_size("type block", name="type length", format="binary", length=1, fuzzable=False)

# Long payload, depends on whether SR flag is set
#if s_block_start("long payload long", dep="header", dep_value=16, dep_compare="!&"):
#    s_size("payload block", format="binary", length = 4, fuzzable=False)
#s_block_end()


# Short payload, depends on whether SR flag is set
#if s_block_start("long payload small", dep="header", dep_value=16, dep_compare="&"):
#    s_size("payload block", format="binary", length = 1, fuzzable=False)
#s_block_end()

s_size("payload block", format="binary", length = 1, fuzzable=False)

# Id Length block, depends on whether IL flag is set
#if s_block_start("id length block", dep="header", dep_value=8, dep_compare="!&"):
#    s_size("id block", name="id length", format="binary", length=1, math=lambda x: x/2, fuzzable=False)
#s_block_end()

# Type block
if s_block_start("type block"):
    s_string("U", fuzzable=False)
s_block_end()


# The payload
if s_block_start("payload block"):
    s_string("5555555555", name="text", encoding="hex", fuzzable=True)
s_block_end()


self.add_protocol_struct("NDEF Dialer")
