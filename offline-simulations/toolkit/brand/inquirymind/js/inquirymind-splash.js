// Copyright 2026, InquiryMind.

/**
 * Preload for the inquirymind brand: gives the loading screen the InquiryMind purple and shows a credit to PhET in the
 * bottom-right corner while the simulation loads. Runs after joist/js/splash.js.
 */
( function() {
  const style = document.createElement( 'style' );
  style.textContent = 'body{background-color:#3d25c4 !important}' +
                      'div:has(> #splash-container){background-color:#3d25c4 !important}';
  document.head.appendChild( style );

  const credit = document.createElement( 'div' );
  credit.textContent = 'Adapted from PhET Interactive Simulations, University of Colorado Boulder';
  credit.setAttribute( 'style', 'position:fixed;right:14px;bottom:10px;z-index:10001;' +
                                'font:13px/1.3 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;' +
                                'color:rgba(255,255,255,.78);pointer-events:none;text-align:right;max-width:70vw' );
  document.body.appendChild( credit );

  const splash = window.phetSplashScreen;
  if ( splash && splash.dispose ) {
    const dispose = splash.dispose;
    splash.dispose = function() {
      credit.remove();
      style.remove();
      return dispose.apply( this, arguments );
    };
  }
} )();
