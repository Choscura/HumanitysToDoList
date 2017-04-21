"""
Sun-tracking software docspec!

basic premise:
    this software should enable a solar unit to be aimed continuously at the sun throughout the day, to correct and optimize that visually, and track sun position with dual feedback from inputted google earth API data corrected by feedback that points the collector more accurately at the sun.

    Advanced version
        actuatable variables
            focal length
            z-axis rotation
            x-axis rotation
        standard tracked variables
            z-motor position
            x-motor position
            collector heading <vector direction turret is pointing>
            device orientation <inferred from collector heading and google earth data; it should be possible to pinpoint location, at least latitudinally, (north south?), based on position of the sun without any other factors, assuming that an accurate rotational model of the earth can be included in the software <if Trump nukes us all, I want these things to outlast the human species

    idea blurbs
        I want there to be a camera, ideally maybe even a thermal camera (assuming the price were low enough?) that could focus on the heat sync assembly and see the exact spot where the sunlight is focused, so that rather than the position of the sun alone, the focal spot of it on the heat sync can be moved across to spread heat evenly across the surface area.

"""
