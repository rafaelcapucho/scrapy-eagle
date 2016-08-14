const initialState = {
  servers_qty: 0,
};

export const INCREASE_SERVER = 'INCREASE_SERVER';
export const SET_SERVER_QTY = 'SET_SERVER_QTY';

export default function stats(state = initialState, action) {

  switch (action.type) {

    case INCREASE_SERVER:

      return Object.assign({}, state, {
        servers_qty: state.servers_qty + 1
      });

    case SET_SERVER_QTY:

      return Object.assign({}, state, {
        servers_qty: action.qty
      });

    default:
      return state;
  }
}