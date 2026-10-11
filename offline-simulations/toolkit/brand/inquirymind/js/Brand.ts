// Copyright 2026, InquiryMind. Brand definition based on brand/adapted-from-phet (MIT, University of Colorado Boulder).

/**
 * Branding for InquiryMind builds of simulations adapted from PhET Interactive Simulations.
 */

import Property from '../../../axon/js/Property.js';
import type { LinkObject } from '../../js/getLinks.js';
import brand from '../../js/brand.js';
import TBrand from '../../js/TBrand.js';
import logo_png from '../images/logo_png.js';
import logoOnWhite_png from '../images/logoOnWhite_png.js';

const Brand: TBrand = {
  id: 'inquirymind',
  name: 'InquiryMind',
  copyright: 'Not an official PhET release. PhET does not endorse InquiryMind.',
  license: 'Adapted from simulations by <a href="https://phet.colorado.edu"><u>PhET Interactive Simulations</u></a>, University of Colorado Boulder, ' +
           'licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (<a href="https://creativecommons.org/licenses/by-nc/4.0/"><u>CC BY-NC 4.0</u></a>).',
  licenseWithoutLinks: 'Adapted from simulations by PhET Interactive Simulations, University of Colorado Boulder (https://phet.colorado.edu), ' +
                       'licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0). https://creativecommons.org/licenses/by-nc/4.0/',
  getLinks: function(): LinkObject[] {
    return [ {
      textStringProperty: new Property( 'Visit InquiryMind' ),
      url: 'https://www.inquirymind.org'
    }, {
      textStringProperty: new Property( 'Original simulations: PhET Interactive Simulations' ),
      url: 'https://phet.colorado.edu'
    } ];
  },
  logoOnBlackBackground: logo_png,
  logoOnWhiteBackground: logoOnWhite_png
};

brand.register( 'Brand', Brand );

export default Brand;
