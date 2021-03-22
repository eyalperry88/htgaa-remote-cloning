metadata = {
    'protocolName': 'Opentrons Logo',
    'author': 'Opentrons <protocols@opentrons.com>',
    'source': 'Protocol Library',
    'apiLevel': '2.9'
}

def run(protocol):

    # Load labware

    # Tips
    tips_20ul = protocol.load_labware(
        'opentrons_96_tiprack_20ul',
        '3',
        'Opentrons 20uL Tips')


    tips_300ul = protocol.load_labware(
        'opentrons_96_tiprack_300ul',
        '6',
        'Opentrons 20uL Tips')


    # DNase/RNase-Free Water Reservoir
    water_container = protocol.load_labware(
        'usascientific_12_reservoir_22ml',
        '1',
        'Water Source')


    # Modules

    temperature_module = protocol.load_module('temperature module gen2', 4)

    thermocycler_module = protocol.load_module('thermocycler')


    # Cold tray
    cold_tray = temperature_module.load_labware('opentrons_24_aluminumblock_generic_2ml_screwcap', label='Cold Tray')

    # Reaction Plate
    reaction_plate = thermocycler_module.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', label='Reaction Plate')


    # -------
    # We need to configure our modules. We will use the temperature module as an "ice block" - it will keep all of our reagents and enzymes nice and cool at 4C until we are ready to mix them. The cell will finish executing only when it reaches the desired temperature - which would take a few minutes. There's a good chance the TA will already set the module to 4C before you start to save time.
    #
    # For the Thermocycler module - we open the lid and set the lid temperature to 102C. Lid temperature is different than the block temperature. The goal of lod temperature is to prevent evaporation of the reaction as it goes through elevated temperature. Since the lid is always hotter than the reaction, we minimize any evaporation.

    # In[3]:


    # Configure modules. This will take a few minutes if the modules are not already at 4C

    # Set cold tray to 4C
    temperature_module.set_temperature(4)

    # Open Thermocycler lid
    thermocycler_module.open_lid()

    # Set *Lid* temperature to 102C
    thermocycler_module.set_lid_temperature(102)

    # And set the Block temperature to 4C
    thermocycler_module.set_block_temperature(4)


    # Now, pipettes. We will use two pipette for this experiment.
    #
    # Available ranges:
    # - P20: 1 µL - 20 µL
    # - P300: 20 µL - 300 µL

    # In[4]:


    # Load pipettes
    pipette_20ul = protocol.load_instrument(
        "p20_single_gen2",
        "left",
        tip_racks=[tips_20ul])

    pipette_300ul = protocol.load_instrument(
        "p300_single",
        "right",
        tip_racks=[tips_300ul])
